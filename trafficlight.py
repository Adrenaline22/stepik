import javax.swing.*;
import java.awt.*;

public class TrafficLight extends JPanel {

@Override
protected void paintComponent(Graphics g) {
super.paintComponent(g);

// Draw the traffic light box
g.setColor(Color.BLACK);
g.fillRect(100, 50, 100, 260);

// Red light
g.setColor(Color.RED);
g.fillOval(120, 60, 60, 60);

// Yellow light
g.setColor(Color.YELLOW);
g.fillOval(120, 140, 60, 60);

// Green light
g.setColor(Color.GREEN);
g.fillOval(120, 220, 60, 60);
}

public static void main(String[] args) {
JFrame frame = new JFrame("Traffic Light");
TrafficLight light = new TrafficLight();

frame.add(light);
frame.setSize(300, 400);
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
frame.setVisible(true);
}
}