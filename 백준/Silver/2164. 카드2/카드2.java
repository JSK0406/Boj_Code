import java.io.*;
import java.util.*;

public class Main  {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        Deque<Integer> q = new LinkedList<>();

        for (int i = 1; i < N+1; i++) {
            q.add(i);
        }

        while (q.size() > 1) {
            q.poll();
            if (q.size() == 1) {
                break;
            }
            q.add(q.poll());
        }

        bw.write(String.valueOf(q.peek()));
        bw.flush();
        bw.close();
    }
}