import java.io.*;
import java.util.*;

public class Solution {
	static int N;
	static int[][] worms;
	static long totalX, totalY;
	static long result;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine().trim());
		for (int t = 1; t <= T; t++) {
			N = Integer.parseInt(br.readLine().trim());
			worms = new int[N][2];
			totalX = 0;
			totalY = 0;
			result = Long.MAX_VALUE;

			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine().trim());
				worms[i][0] = Integer.parseInt(st.nextToken());
				worms[i][1] = Integer.parseInt(st.nextToken());
				totalX += worms[i][0];
				totalY += worms[i][1];
			}

			// 0번 지렁이는 출발 그룹에 고정
			dfs(1, 1, worms[0][0], worms[0][1]);

			sb.append("#").append(t).append(" ").append(result).append("\n");
		}
		System.out.print(sb);
	}

	private static void dfs(int idx, int cnt, long sx, long sy) {
		if (cnt == N / 2) {
			long x = totalX - 2 * sx;
			long y = totalY - 2 * sy;
			result = Math.min(result, x * x + y * y);
			return;
		}
		if (idx == N) return;
		
		// 남은 지렁이로 N/2를 못 채우면 가지치기
		if (N - idx < N / 2 - cnt) return;

		// idx를 출발 그룹에 넣기
		dfs(idx + 1, cnt + 1, sx + worms[idx][0], sy + worms[idx][1]);
		
		// idx를 도착 그룹에 넣기
		dfs(idx + 1, cnt, sx, sy);
	}
}