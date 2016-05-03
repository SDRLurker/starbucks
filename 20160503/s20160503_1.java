import java.util.Scanner;

public class s20160503_1 {
	public int del_num(String a, String b) {
		int[] a_num = new int[26]; 
		int[] b_num = new int[26]; 

		for(int i=0;i<a.length();i++)
			a_num[a.charAt(i) - 'a']++;
		for(int i=0;i<b.length();i++)
			b_num[b.charAt(i) - 'a']++;
		int dels = 0;
		for(int i=0;i<26;i++)
			dels += Math.abs(a_num[i] - b_num[i]);
		return dels;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String a = sc.next();
		String b = sc.next();
		System.out.println(new s20160503_1().del_num(a,b));
	}
}
