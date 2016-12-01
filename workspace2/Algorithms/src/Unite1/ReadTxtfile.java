package Unite1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class ReadTxtfile {
	private static Stream<String> stream;

	public static void main(String[] args) throws IOException {
		String filepath = "/home/xue/tinyW.txt";
		stream = Files.lines(Paths.get(filepath));
		try {
			stream.forEach(System.out::println);
			
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	}

}
