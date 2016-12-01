package unite7;

import static mindview.Print.*;

class Insect {
	private int i = 9;
	protected int j;
	public Insect() {
		print("i = " + i + ", j = " + j);
		j = 39;
		
	}
	private static int x1 = 
			printInit("static Insect.x1 initalizationed");
	static int printInit(String s) {
		print(s);
		return 47;
	}
}

public class Beetle extends Insect {
	private static int k = 
			printInit("static Insect.k initalizationed");
	public Beetle() {
		// TODO Auto-generated constructor stub
		print("k = " + k);
		print("j = " + k);
	}
	private static int x2 = 
			printInit("static Insect.x2 initalizationed");
	public static void main(String[] args) {
		print("Better Constructor");
		Beetle b = new Beetle();
	}
	

}















