import javax.swing.*;
import java.awt.*;

public class Snowman extends JPanel {

@Override
protected void paintComponent(Graphics g) {
super.paintComponent(g);

// Draw bottom circle
g.setColor(Color.WHITE);
g.fillOval(100, 150, 200, 200);

// Draw middle circle
g.fillOval(130, 100, 140, 140);

// Draw top circle (head)
g.fillOval(160, 50, 80, 80);

// Draw eyes
g.setColor(Color.BLACK);
g.fillOval(180, 75, 10, 10);
g.fillOval(210, 75, 10, 10);

// Draw mouth
g.drawArc(180, 95, 40, 20, 0, -180);

// Draw buttons
g.fillOval(190, 130, 20, 20);
g.fillOval(190, 170, 20, 20);
g.fillOval(190, 210, 20, 20);
}

public static void main(String[] args) {
JFrame frame = new JFrame("Snowman");
Snowman snowman = new Snowman();

frame.add(snowman);
frame.setSize(400, 400);
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
frame.setVisible(true);
}
}