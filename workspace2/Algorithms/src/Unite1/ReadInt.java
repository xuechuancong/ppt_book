package Unite1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadInt {
	public static String 
	readint(String filename) throws IOException{
		BufferedReader in = new BufferedReader(new FileReader(filename));
		String s;
		StringBuilder sb = new StringBuilder();
		while((s = in.readLine()) != null)
			sb.append(s + "\n");
		in.close();
		System.out.println(sb);
		return sb.toString();		
	}
	public static void main(String[] args) 
	throws IOException{
		System.out.println(readint("/home/xue/Hello.txt"));
//		System.out.println();
	}

}
