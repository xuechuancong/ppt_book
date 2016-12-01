package Unite1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class TestReadfile {
	public static void main(String args[]) {

		String filepath = "/home/xue/Hello.txt";

		//read file into stream, try-with-resources
		try (Stream<String> stream = Files.lines(Paths.get(filepath))) {

			stream.forEach(System.out::println);

		} catch (IOException e) {
			e.printStackTrace();
		}

	}


}
