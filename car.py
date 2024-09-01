import javax.swing.*;
import java.awt.*;

public class Car extends JPanel {

@Override
protected void paintComponent(Graphics g) {
super.paintComponent(g);

// Draw car body
g.setColor(Color.BLUE);
g.fillRect(100, 200, 200, 50);

// Draw car roof
g.fillRect(150, 150, 100, 50);

// Draw wheels
g.setColor(Color.BLACK);
g.fillOval(120, 240, 50, 50);
g.fillOval(230, 240, 50, 50);
}

public static void main(String[] args) {
JFrame frame = new JFrame("Car");
Car car = new Car();

frame.add(car);
frame.setSize(400, 400);
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
frame.setVisible(true);
}
}