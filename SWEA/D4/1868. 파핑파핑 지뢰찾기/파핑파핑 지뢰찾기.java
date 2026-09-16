import java.io.*;
import java.util.*;

public class Solution {
	
	static int N;
	static char[][] board;
	
	// 상 우상 우 .. 
	static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
	static int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine());
			board = new char[N][N];
			
			for (int i = 0; i < N; i++) {
				board[i] = br.readLine().trim().toCharArray();
			}
			
			/*
			 * 지뢰가 아닌 모든 영역을 클릭하기
			 * 최소 클릭 횟수 구하기
			 * * 0 인 부분 찾아서 bfs로 연쇄 초기화 먼저 하기
			 * * 남은 모든 지뢰의 칸 수 + 0 초기화 진행 횟수가 답
			 */
			
			int cnt = 0;
			boolean[][] visited = new boolean[N][N];
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					// 이미 클릭되었으면 확인 안함 
					if (visited[i][j]) continue;
					if (board[i][j] == '.' && bombCount(i,j) == 0) {
						// 클릭하기
						cnt++;
						visited[i][j] = true;
						chaining(i,j,visited);
					}
				}
			}
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (board[i][j] == '.' && !visited[i][j]) cnt++;
				}
			}
			
			StringBuilder sb = new StringBuilder();
			sb.append("#").append(tc).append(" ").append(cnt);
			System.out.println(sb);
			
		}
		
		
		
	}
	
	static void chaining(int x, int y, boolean[][] visited) {
		Deque<int[]> deq = new ArrayDeque<>();
		deq.offerLast(new int[] {x,y});
		
		while (!deq.isEmpty()) {
			
			int[] idx = deq.pollFirst();
			int r = idx[0];
			int c = idx[1];
			
			for (int i = 0; i < dx.length; i++) {
				int nr = r + dx[i];
				int nc = c + dy[i];
				// 이미 조사한 곳은 범위에 미추가
				if (!isInRange(nr,nc)) continue;
				if (visited[nr][nc]) continue;
				visited[nr][nc] = true;
				int cnt = bombCount(nr, nc);
				if (cnt == 0) {
					deq.offerLast(new int[] {nr, nc});
				} 
				if (cnt != 0) continue;
			}
			
		}
	}
	
	static int bombCount(int x, int y) {
		int cnt = 0;
		
		for (int i = 0; i < dx.length; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (!isInRange(nx, ny)) continue;
			if (board[nx][ny] == '*') cnt++;
		}
		
		return cnt;
	}
	
	static boolean isInRange(int x, int y) {
		return (x >= 0 && x < N && y >= 0 && y < N);
	}
	
}