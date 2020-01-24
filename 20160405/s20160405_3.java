import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class s20160405_3 {
    private boolean isAnagram(String a, String b) {
        byte a_num[] = new byte[26];
        byte b_num[] = new byte[26];
        if(a.length()!=b.length())
            return false;
        for(int i=0;i<a.length();i++) {
            a_num[a.charAt(i) - 'a']++;
            b_num[b.charAt(i) - 'a']++;
        }
        return Arrays.equals(a_num, b_num);
    }
    
    public int getPairs(String s) {
        int pairs = 0;
        int len = s.length();
        for(int li=1;li<len;li++) {
            for(int i=0;i<len-li;i++) {
                for(int j=i+1;j<len-li+1;j++) {
                    if(isAnagram(s.substring(i,i+li), s.substring(j,j+li)))
                        pairs++;
                }
            }
        }
        return pairs;
    }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for(int i=0;i<n;i++) {
            s20160405_3 solution = new s20160405_3();
            System.out.println(solution.getPairs(in.next()));
        }
    }
}
