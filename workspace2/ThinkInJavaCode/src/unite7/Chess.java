package unite7;
import static mindview.Print.*;


class Game {
	Game(int i) {
		print(" Game Constructor ");
	}
}

class BoardGame extends Game {
	BoardGame(int i) {
		super(i);
		print(" BoardGame ");
		
	}
}
public class Chess extends BoardGame {
	public Chess() {
		super(4);
		print(" Chess Constructor");		
	}
	public static void main(String[] args) {
		Chess x = new Chess();
		print(x);
	}

}
