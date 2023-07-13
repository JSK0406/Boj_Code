import java.io.*;
import java.util.*;

public class Main  {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        Deque<String> q = new LinkedList<>();
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String com = st.nextToken();
            if (com.equals("push")) {
                q.add(st.nextToken());
            } else if (com.equals("pop")) {
                String tmp = q.poll();
                if (tmp != null) {
                    bw.write(tmp + "\n");
                } else {
                    bw.write("-1" + "\n");
                }
            } else if (com.equals("size")) {
                bw.write(q.size() + "\n");
            } else if (com.equals("empty")) {
                if (q.size() > 0) {
                    bw.write("0" + "\n");
                } else {
                    bw.write("1" + "\n");
                }
            } else if (com.equals("front")) {
                String tmp = q.peek();
                if (tmp != null) {
                    bw.write(tmp + "\n");
                } else {
                    bw.write("-1" + "\n");
                }
            } else if (com.equals("back")) {
                String tmp = q.peekLast();
                if (tmp != null) {
                    bw.write(tmp  + "\n");
                } else {
                    bw.write("-1" + "\n");
                }
            }
        }
    bw.flush();
    }
}