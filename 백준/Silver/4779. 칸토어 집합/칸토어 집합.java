import java.io.*;
import java.util.*;
import java.math.*;

public class Main  {

        public static String recur(int n) {
            if (n == 0) {
                return "-";
            }
            else {
                return recur(n-1) + " ".repeat((int)Math.pow(3,(n-1))) + recur(n-1);
            }
        }



    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while (true) {
            try {
                int N = Integer.parseInt(br.readLine());
                String result = recur(N);
                bw.write(result + "\n");

            } catch (Exception err) {
                break;
            }
        }
        bw.flush();
        bw.close();
    }
}