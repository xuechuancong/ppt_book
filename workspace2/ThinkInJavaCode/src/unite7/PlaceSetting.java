package unite7;

import static mindview.Print.*;

class Plate {
	public Plate(int i) {
		print(" Plate Constructor");
	}
}
class DinnerPlate extends Plate {
	public DinnerPlate(int i) {
		super(i);
		print(" DinnerPlate Constructor");
	}
}
class Utensil {
	public Utensil(int i) {
		// TODO Auto-generated constructor stub
		print(" Utensil Constructor");
	}
}
class Spoon extends Utensil {
	public Spoon(int i) {
		// TODO Auto-generated constructor stub
		super(i);
		print(" Spoon Constructor");
	}
}
class Fork extends Utensil {
	public Fork(int i) {
		// TODO Auto-generated constructor stub
		super(i);
		print(" Fork Constructor");
	}
}
class Knife extends Utensil {
	public Knife(int i) {
		// TODO Auto-generated constructor stub
		super(i);
		print(" Knife Constructor");
	}
}
class Custom {
	public Custom(int i) {
		// TODO Auto-generated constructor stub
		print(" Custom Constructor");
	}
}

public class PlaceSetting extends Custom {
	private Spoon sp;
	private Fork frk;
	private Knife kn;
	private DinnerPlate pl;
	public PlaceSetting(int i) {
		// TODO Auto-generated constructor stub
		super(i + 1);
		sp = new Spoon(i + 2);
		frk = new Fork(i + 3);
		kn = new Knife(i + 4);
		pl = new DinnerPlate(i + 5);
		print(" PlaceSetting Constructor");
	}

	public static void main(String[] args) {
		PlaceSetting x = new PlaceSetting(3);
	}


}


















