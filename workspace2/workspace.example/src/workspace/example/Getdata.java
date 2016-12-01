package workspace.example;


public class Getdata {
	public static void main(String[] args){
                int num=10;
		outer: for (int i = 3; i < num; i++) {
			for (int j = 2; j < i; j++) {
				if (i%j==0) {
					continue outer;
					
				}
				
			}
			System.out.println(" "+i);
			
		}
	}

}	
	
			
		
	



