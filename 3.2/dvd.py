import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class MovingImageDVD extends JPanel implements ActionListener {

private Image image;
private int x = 0, y = 0; // Начальные координаты изображения
private int xSpeed = 3, ySpeed = 3; // Скорость движения по осям x и y

private Timer timer;

public MovingImageDVD() {
try {
// Загружаем изображение
image = ImageIO.read(new File("photo.png"));
} catch (IOException e) {
System.out.println("Image not found or unable to read the image file.");
e.printStackTrace();
}

timer = new Timer(20, this); // Таймер, вызывающий ActionListener каждые 20 миллисекунд
timer.start();
}

@Override
protected void paintComponent(Graphics g) {
super.paintComponent(g);

if (image != null) {
// Рисуем изображение на текущих координатах (x, y)
g.drawImage(image, x, y, this);
}
}

@Override
public void actionPerformed(ActionEvent e) {
// Обновляем координаты с учетом скорости
x += xSpeed;
y += ySpeed;

// Проверяем столкновения с краями окна и меняем направление
if (x <= 0 || x + image.getWidth(this) >= getWidth()) {
xSpeed = -xSpeed; // Меняем направление по оси X
}
if (y <= 0 || y + image.getHeight(this) >= getHeight()) {
ySpeed = -ySpeed; // Меняем направление по оси Y
}

// Перерисовываем компонент с новыми координатами
repaint();
}

public static void main(String[] args) {
JFrame frame = new JFrame("DVD Logo Simulation");
MovingImageDVD panel = new MovingImageDVD();

frame.add(panel);
frame.setSize(800, 600); // Размер окна
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
frame.setVisible(true);
}
}