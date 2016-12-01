package Unite2;

public class p10_01 {
	public static void BQBJ(int m, int n) {
		int z;
		for (int x = 0; x <= m; x++) {
			for (int y = 0; y <= m; y++) {
				z = m-x-y;
				if (z > 0 && z%3==0 && x*5+y*3+z/3==n) {
					System.out.printf("公鸡: %d只， 母鸡： %d只， 小鸡： %d只\n", x, y, z );
				}
				else {}
			}
		}
	}
	public static void main(String[] args) {
		BQBJ(100, 100);
	}

}
