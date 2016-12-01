package Unite5;

public class Burrito {
	Spiciness degree;
	public Burrito(Spiciness degree) { this.degree = degree;}
	public void describe() {
		System.out.println("This burrito is ");
		switch (degree) {
		case NOT:  System.out.println("not spicy at all.");
			break;
		case MILD:  
			break;
		case MEDIUM: System.out.println("a little hot");
			break;
		case HOT: 
		case FLAMING:			
		default:  System.out.println("maybe too hot.");
			
		}
	}
	
	public static void main(String[] args) {
		Burrito plain, greenChile, jalapenp;
		plain = new Burrito(Spiciness.NOT);
		greenChile = new Burrito(Spiciness.MEDIUM);
		jalapenp = new Burrito(Spiciness.HOT);
		plain.describe();
		greenChile.describe();
		jalapenp.describe();
		  
	}

}














