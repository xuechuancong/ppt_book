package unite7;

class Watersource {
	private String s;
	Watersource() {
		System.out.println("watersource()");
		s = "Constructed";
	}
	public String toString() {
		return s;
	}
}

public class SprinklerSystem {
	private String v1, v2, v3, v4;
	private Watersource source = new Watersource();
	private int i;
	private float f;
	public String toString() {
		return
				"v2 = " + v1 + " " +
				"v2 = " + v2 + " " +
				"v3 = " + v3 + " " +
				"v4 = " + v4 + "\n" +
				"i = " + i + " " + "f = " + f + " " +
				"source = " + source;
 	}
	public static void main(String[] args) {
		SprinklerSystem sprinker = new SprinklerSystem();
		System.out.println(sprinker);
	}

}










