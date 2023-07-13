import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        List<Integer> lst = new ArrayList<>();

        for (int i = 0; i < N + 1; i++) {
            lst.add(i);
        }


        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int tmp = lst.get(a);
            lst.set(a, lst.get(b));
            lst.set(b, tmp);
        }

        for (int i: lst.subList(1, lst.size())) {
            System.out.print(i + " ");
        }
        
    }
}