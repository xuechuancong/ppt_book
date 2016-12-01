package Unite5;

class Book {
	boolean checkedOut = false;//开始每本书都没有签入--初始化
	public Book(boolean checkOut) {
		// TODO Auto-generated constructor stub
		checkedOut = checkOut;//判断这本书是否签入
	}
	void checkIn() {//签入这本书
		checkedOut = false;
	}
	protected void finalize() {
		if (checkedOut) {//如果没有签入的话就报错
			System.out.println("Error: checked out");
		}
	}
}


public class TerminationCondition {
	public static void main(String[] args) {
		Book novel = new Book(true);//一个新的novel对象--继承自Book
		novel.checkIn();//对每本书签入
		new Book(true);//一本书没有签入
		System.gc();//强行结束终止动作
	}

}












