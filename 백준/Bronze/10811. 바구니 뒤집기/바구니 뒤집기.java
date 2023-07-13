import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());  // 바구니 개수
        int M = Integer.parseInt(st.nextToken());  // 순서 개수
        LinkedList<Integer> lst = new LinkedList<>();

        for (int i = 0; i < N+1; i++) {
            lst.add(i);
        }


        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            List<Integer> tmpLst = lst.subList(a, b+1);
            Collections.reverse(tmpLst);
            for (int j = a; j < b + 1; j++) {
                lst.set(j, tmpLst.get(j-a));
            }
        }

        for (int i : lst.subList(1, lst.size())) {
            System.out.print(i + " ");
        }
    }

}