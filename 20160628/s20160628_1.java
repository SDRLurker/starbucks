class Solution {
    public boolean isPerfectSquare(int num) {
        if(num == 1)
            return true;
        int left = 1;
        int right = num;
        while(left <= right) {
            int mid = (left + right) / 2;
            // mid가 46341 이상이면 제곱시 오버플로우 발생.
            if(mid >= 46341 || mid * mid > num)
                right = mid - 1;
            else if(mid * mid < num)
                left = mid + 1;
            else
                return true;
        }
        return false;
    }
}

public class s20160628_1 {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.printf("%5s %10s %10s\n","input","Expected","Result");
        System.out.printf("%5d %10s %10s\n",16,"true",s.isPerfectSquare(16));
        System.out.printf("%5s %10s %10s\n","input","Expected","Result");
        System.out.printf("%5d %10s %10s\n",14,"false",s.isPerfectSquare(14));
    }
}
