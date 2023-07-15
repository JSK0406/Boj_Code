import java.io.*;
import java.util.*;
import java.math.*;

public class Main  {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        while (!str.equals("0")) {
            int j = str.length() - 1;
            for (int i = 0; i < str.length(); i++) {
                    if (i >= j) {
                        bw.write("yes" + "\n");
                        break;
                    } else {
                        if (str.charAt(i) == str.charAt(j)) {
                            j--;
                            continue;
                        } else {
                            bw.write("no" + "\n");
                            break;
                        }
                    }
            }
            str = br.readLine();
        }
        bw.flush();
        bw.close();
    }


}