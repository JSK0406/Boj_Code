import java.io.*;
import java.util.*;

public class Main  {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<String> stack = new Stack<>();
        stack.add("ABC");

        String sentence = br.readLine();

        boolean Flag = true;
        while (sentence.equals(".") == false) {
            for (String str : sentence.split("")) {
                if (str.equals("(") || str.equals("[")) {
                    stack.push(str);
                } else if (str.equals(")")) {
                    if (stack.peek().equals("(")) {
                        stack.pop();
                    } else {
                        Flag = false;
                        break;
                    }
                } else if (str.equals("]")) {
                    if (stack.peek().equals("[")) {
                        stack.pop();
                    } else {
                        Flag = false;
                        break;
                    }
                }
            }
            if (Flag == false || !stack.peek().equals("ABC")) {
                bw.write("no" + "\n");

            } else {
                bw.write("yes" + "\n");
            }
            sentence = br.readLine();
            Flag = true;
            stack = new Stack<>();
            stack.add("ABC");
        }
    bw.flush();

    }
}