package unite7;

import static mindview.Print.*;

class Soup {
	private String s;
	public Soup() {
		print("Soup()");
		s = "Constructed";
	}
	public String toString() {
		return s;
	}
}

public class Bath {
	private String
	  s1 = "Happy",
	  s2 = "Happy",
	  s3, s4;
	private Soup castille;//一个Soup对象
	private int i;
	private float toy;
	public Bath() {
		print("Inside Bath()");
		setS3("Joy");
		toy = 3.14f;
		castille = new Soup();
	}
	{i = 47;}
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		if (s4 == null) {
			s4 = "Joy";
		}
		return 
				"s1 = " + s1 + "\n" +
		        "s2 = " + s2 + "\n" +
				"s3 = " + s4 + "\n" + 
		        "s4 = " + s4 + "\n" +
				"i = " + i + "\n" +
		        "toy = " + toy + "\n" +
				"castille = " + castille; 
	}
	public static void main(String[] args) {
		Bath b = new Bath();
		print(b);
	}
	public String getS3() {
		return s3;
	}
	public void setS3(String s3) {
		this.s3 = s3;
	}

}









