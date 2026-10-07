import java.io.*;
import java.util.*;

public class Solution {
	
	static int N;
	static int K;
	static int[][] board;
	static int answer;
	
	static int[] dr = {-1, 0, 1, 0};
	static int[] dc = {0, 1, 0, -1};
	static boolean[][] visited;
	
	public static void main(String[] args) throws Exception {
		/*
		 * 최고 높이 인덱스에서 dfs
		 * 4방향 탐색, 낮은 값으로만 이동가능
		 * dfs한번 당 1회 최대 k 깊이 공사가능
		 * 이미 갈 수 있는 곳은 공사 x, 못가는 곳 공사 -> 현 위치 -1 값으로 공사할 수 있다면 최소 0
		 */
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			board = new int[N][N];
			
			int maximum = 0;
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
					if (board[i][j] > maximum) maximum = board[i][j];
				}
			}
			
			List<int[]> maxIdxs =new ArrayList<>();
			for (int i = 0; i < N; i++) {
				for (int j =0; j < N; j++) {
					if (board[i][j] == maximum) maxIdxs.add(new int[] {i,j});
				}
			}
			
			answer = 0;
			for (int[] idx: maxIdxs) {
				visited = new boolean[N][N];
				visited[idx[0]][idx[1]] = true;
				dfs(idx[0], idx[1], false, 1);
			}
			StringBuilder sb = new StringBuilder();
			sb.append("#").append(tc).append(" ").append(answer);
			System.out.println(sb);
		}
	}
	
	static void dfs(int r, int c, boolean useK, int depth) {
		
		if (depth > answer) answer = depth;
		
		for (int i = 0; i < dr.length; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];
			if (!isInRange(nr, nc)) continue;
			if (visited[nr][nc]) continue;
			if (board[nr][nc] < board[r][c]) {
				// 진행 가능
				visited[nr][nc] = true;
				dfs(nr, nc, useK, depth + 1);
				visited[nr][nc] = false;
			}
			else {
				// 공사 가능할 경우
				if (!useK && board[nr][nc] - K < board[r][c]) {
					int origin = board[nr][nc];
					useK = true;
					board[nr][nc] = board[r][c] - 1;
					visited[nr][nc] = true;
					dfs(nr, nc, useK, depth + 1);
					useK = false;
					board[nr][nc] = origin;
					visited[nr][nc] = false;
				}
			}
		}
	}
	
	static boolean isInRange(int r, int c) {
		return (r >= 0 && r < N && c >= 0 && c < N);
	}
}