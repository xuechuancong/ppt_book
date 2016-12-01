package example;

public class getdata {
	public static void main(String[] args) {
		int num=200;
		outer:for(int i=2;i<num;i++){
			for(int j=2; j<i; j++){
				if(i%j==0)
					continue outer;
				}
			System.out.println(" "+i);
			
		}
	}


}
