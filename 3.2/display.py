import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class ImageDisplay extends JPanel {

private Image image;

public ImageDisplay() {
try {
// Load the image from the file system
image = ImageIO.read(new File("photo.png"));
} catch (IOException e) {
System.out.println("Image not found or unable to read the image file.");
e.printStackTrace();
}
}

@Override
protected void paintComponent(Graphics g) {
super.paintComponent(g);

if (image != null) {
// Draw the image at the center of the panel
int x = (getWidth() - image.getWidth(this)) / 2;
int y = (getHeight() - image.getHeight(this)) / 2;
g.drawImage(image, x, y, this);
}
}

public static void main(String[] args) {
JFrame frame = new JFrame("Image Display");
ImageDisplay imagePanel = new ImageDisplay();

frame.add(imagePanel);
frame.setSize(800, 600); // Set the window size
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
frame.setVisible(true);
}
}