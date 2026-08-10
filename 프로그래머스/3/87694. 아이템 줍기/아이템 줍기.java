import java.util.ArrayDeque;

class Solution {

    // 좌표를 2배 하므로 51 -> 102 이상 필요
    public static int[][] board = new int[102][102];

    // BFS에서는 반드시 4방향만 이동
    public static int[] dx = {-1, 0, 1, 0};
    public static int[] dy = {0, 1, 0, -1};

    static class Point {
        int r;
        int c;
        int moving;

        Point(int r, int c, int moving) {
            this.r = r;
            this.c = c;
            this.moving = moving;
        }
    }

    public static boolean inRange(int n, int x, int y) {
        return x >= 0 && x < n
                && y >= 0 && y < n;
    }

    public int solution(
            int[][] rectangle,
            int characterX,
            int characterY,
            int itemX,
            int itemY) {

        // 혹시 solution이 여러 번 호출되어도 안전하도록 초기화
        board = new int[102][102];

        /*
         * 1. 모든 사각형의 "전체 영역"을 먼저 칠한다.
         *
         * board[x][y] == 1
         * → 현재는 사각형 영역이라는 뜻
         */
        for (int[] rec : rectangle) {

            int x1 = rec[0] * 2;
            int y1 = rec[1] * 2;
            int x2 = rec[2] * 2;
            int y2 = rec[3] * 2;

            for (int x = x1; x <= x2; x++) {
                for (int y = y1; y <= y2; y++) {
                    board[x][y] = 1;
                }
            }
        }

        /*
         * 2. 사각형의 내부를 제거한다.
         *
         * 테두리는 건드리면 안 되므로
         *
         * x1 + 1 ~ x2 - 1
         * y1 + 1 ~ y2 - 1
         *
         * 만 0으로 만든다.
         *
         * 그러면 최종적으로 board == 1인 곳은
         * 사각형들의 외곽선만 남는다.
         */
        for (int[] rec : rectangle) {

            int x1 = rec[0] * 2;
            int y1 = rec[1] * 2;
            int x2 = rec[2] * 2;
            int y2 = rec[3] * 2;

            for (int x = x1 + 1; x < x2; x++) {
                for (int y = y1 + 1; y < y2; y++) {
                    board[x][y] = 0;
                }
            }
        }

        /*
         * 3. 시작점과 목표점도 좌표를 2배
         */
        int startX = characterX * 2;
        int startY = characterY * 2;

        int targetX = itemX * 2;
        int targetY = itemY * 2;

        /*
         * board와 visited의 역할을 분리
         *
         * board   = 지형 정보
         * visited = BFS 방문 정보
         */
        boolean[][] visited = new boolean[102][102];

        ArrayDeque<Point> deq = new ArrayDeque<>();

        deq.add(new Point(startX, startY, 0));
        visited[startX][startY] = true;

        /*
         * 4. 테두리(board == 1)만 따라서 BFS
         */
        while (!deq.isEmpty()) {

            Point p = deq.poll();

            int r = p.r;
            int c = p.c;
            int move = p.moving;

            if (r == targetX && c == targetY) {
                // 좌표를 2배 했으므로 거리도 2배
                return move / 2;
            }

            for (int d = 0; d < 4; d++) {

                // 현재 좌표는 변경하지 않고
                // 다음 좌표를 별도로 생성
                int nr = r + dx[d];
                int nc = c + dy[d];

                if (!inRange(board.length, nr, nc)) {
                    continue;
                }

                // 테두리가 아니면 이동 불가
                if (board[nr][nc] != 1) {
                    continue;
                }

                // 이미 방문했다면 이동하지 않음
                if (visited[nr][nc]) {
                    continue;
                }

                visited[nr][nc] = true;

                deq.add(
                    new Point(nr, nc, move + 1)
                );
            }
        }

        return -1;
    }
}