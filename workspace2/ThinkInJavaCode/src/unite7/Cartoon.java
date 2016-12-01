package unite7;

import static mindview.Print.*;

class Art {
	public Art() {
		print(" Art Constructor");
	}
}

class Drawing extends Art {
	public Drawing() {
		print(" Drawing Constructor");
	}
}

public class Cartoon extends Drawing {
	public Cartoon() {
		print(" Cartoon Constructor");
	}
	public static void main(String[] args) {
		@SuppressWarnings("unused")
		Cartoon x = new Cartoon();
	}
}











