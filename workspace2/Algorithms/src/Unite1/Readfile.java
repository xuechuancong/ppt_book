package Unite1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class Readfile {


	private static BufferedReader br;

	public static void main(String[] args) {
		try {// 防止文件建立或读取失败，用catch捕捉错误并打印，也可以throw  
			
			/* 读入TXT文件 */
			String pathname = "/home/xue/Hello.txt"; //文件的绝对路径
			File filename = new File(pathname); //读取上面路径的文件
			InputStreamReader reader = new InputStreamReader(new FileInputStream(filename));
			br = new BufferedReader(reader);
			String line = "";
			line = br.readLine();
			while (line != null) {
				System.out.println(line);
			}
			reader.close();
	
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		
	}

}
