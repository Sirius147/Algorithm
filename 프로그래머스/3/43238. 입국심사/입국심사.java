import java.util.Arrays;
class Solution {
    
    public static long people;
    public static long answer;
    
    public static void binarySearch(long minTime, long maxTime, int[] times){
        while (minTime <= maxTime) {
            long midTime = (minTime+maxTime) / 2l;
            long cnt = 0;
            for (int t: times){
                cnt += (midTime) / (long) t;
            }
            if (cnt >= people) {
                // 시간이 대기인원에 비해 많다.
                // 일단 정답 후보지만, t = 9, times = [2,4]  -> t = 8가 최적인 반례가 있다.
                // 따라서, 정답으로 정해두고, 한번 더 탐색한다.
                answer = midTime;
                maxTime = midTime - 1l;
            } else {
                // 시간이 대기 인원에 비해 부족하다
                minTime = midTime + 1l;
            }
        }
    }
    
    public long solution(int n, int[] times) {
        int judges = times.length;
        Arrays.sort(times);
        long longestTime = times[judges-1];
        long worstTime = longestTime * (long) n;
        people = n;
        binarySearch(1, worstTime, times);
        
        return answer;
    }
}