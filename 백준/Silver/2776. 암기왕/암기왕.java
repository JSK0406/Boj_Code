import java.io.*;
import java.lang.reflect.Type;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            HashMap<String, String> mapN = new HashMap<>();
            int N = Integer.parseInt(br.readLine());
            String[] arrN = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                mapN.put(arrN[j], "1");
            }

            int M = Integer.parseInt(br.readLine());
            String[] arrM = br.readLine().split(" ");
            for (int k = 0; k < M; k++) {
                String tmpPrint = mapN.getOrDefault(arrM[k], "0");
                bw.write(tmpPrint);
                bw.write("\n");
            }

        }
        bw.flush();
    }
}