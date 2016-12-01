package unite7;

public class SpaceShipDelegation {
	private String name;
	private SpaceShipConstrols constrols = new SpaceShipConstrols();
	public SpaceShipDelegation(String name) {
		this.name = name;
	}
	public String toString() {
		return name;
	}
	
	public void back(int velocity) {
		constrols.back(velocity);
	}
	
	public void down(int velocity) {
		constrols.down(velocity);
	}
	
	public void forward(int velocity) {
		constrols.back(velocity);
	}
	
	public void left(int velocity) {
		constrols.left(velocity);
	}
	
	public void right(int velocity) {
		constrols.right(velocity);
	}
	
	public void turboBoost(int velocity) {
		constrols.turboBoost(velocity);
	}
	
	public void up(int velocity) {
		constrols.back(velocity);
	}
	
	public static void main(String[] args) {
		SpaceShipDelegation protector = new SpaceShipDelegation("NSEA Protector");
		protector.forward(100);
	}
	
	

}
