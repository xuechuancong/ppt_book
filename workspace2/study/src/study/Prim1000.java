package study;

public class Prim1000 {
	public static void main(String[] args) {
		outer: for (int i = 3; i < 1000; i++) {
			for (int j = 2; j < i; j++) {
				if (i%j==0) {
					continue outer;
					
				}
				
			}
			System.out.print(" "+i);
		}
	}

}
