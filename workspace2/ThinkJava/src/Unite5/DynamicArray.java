package Unite5;

public class DynamicArray {
	public static void main(String[] args) {
		Other.main(new String[] {"fiddle", "de", "dum"});//调用main函数
	}
}	
class Other {
	public static void main(String[] args) {
		for(String s : args)
			System.out.println(s + " ");
	}
}



