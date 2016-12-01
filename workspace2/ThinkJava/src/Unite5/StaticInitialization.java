package Unite5;

class Bowl {
	public Bowl(int marker) {
		// TODO Auto-generated constructor stub
		System.out.println(Messages.getString("StaticInitialization.0") + marker + Messages.getString("StaticInitialization.1")); //$NON-NLS-1$ //$NON-NLS-2$
	}
	void f1(int marker) {
		System.out.println(Messages.getString("StaticInitialization.2") + marker + Messages.getString("StaticInitialization.3")); //$NON-NLS-1$ //$NON-NLS-2$
	}
}

class Table {
	static Bowl bowl1 = new Bowl(1);
	public Table() {
		// TODO Auto-generated constructor stub
		System.out.println(Messages.getString("StaticInitialization.4")); //$NON-NLS-1$
		bowl2.f1(1);
	}
	void f2(int marker) {
		System.out.println(Messages.getString("StaticInitialization.5") + marker + Messages.getString("StaticInitialization.6")); //$NON-NLS-1$ //$NON-NLS-2$
	}
	static Bowl bowl2 = new Bowl(2);
}

class Cupboard {
	Bowl bowl3 = new Bowl(3);
	static Bowl bowl4 = new Bowl(4);
	public Cupboard() {
		// TODO Auto-generated constructor stub
		System.out.println(Messages.getString("StaticInitialization.7")); //$NON-NLS-1$
		bowl4.f1(2);
	}
	static Bowl bowl5 = new Bowl(5);
	public void f3(int marker) {
		// TODO Auto-generated method stub
		System.out.println(Messages.getString("StaticInitialization.8") + marker + Messages.getString("StaticInitialization.9")); //$NON-NLS-1$ //$NON-NLS-2$
		
	}
}
public class StaticInitialization {
	public static void main(String[] args) {
		System.out.println(Messages.getString("StaticInitialization.10")); //$NON-NLS-1$
		new Cupboard();
		System.out.println(Messages.getString("StaticInitialization.11")); //$NON-NLS-1$
		new Cupboard();
		table.f2(1);
		cupboard.f3(1);
	}
	static Table table = new Table();
	static Cupboard cupboard = new Cupboard();


}












