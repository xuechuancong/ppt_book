package study;


public class Getprime {
	public static void main(String[] args) {//建立一个长度为1000的数组并赋值为2-1001
		int[] a = new int[1000];
		for (int i = 2; i < a.length+2; i++) {
			a[i-2] = i;
			
		}
		int n = 0;
		outer: for(int num:a){//增强的for语句遍历数组a
			//System.out.print(" "+num);
			for (int j = 2; j < num; j++) {//埃氏筛法求素数
				if (num%j==0) {
					continue outer;
				}
				
			}
			System.out.print(" "+num);
            n++;
            if (n < 10) continue;
            System.out.println( );
            n = 0;
            
            	
		}
	}
}
