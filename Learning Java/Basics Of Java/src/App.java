//import java.awt.Container;
//import java.awt.Dimension;
//import java.awt.event.ActionEvent;
//import java.awt.event.ActionListener;
//import java.util.Dictionary;
//import javax.swing.ImageIcon;
//import javax.swing.JButton;
//import javax.swing.JFrame;
//import javax.swing.JMenu;
//import javax.swing.JMenuBar;
//import javax.swing.JMenuItem;
//import javax.swing.JOptionPane;
//import javax.swing.JToolBar;
//import javax.swing.KeyStroke;
//
//
//
//public class App{
//    extends JFrame{
//        public MenuFrame(){
//            throws Exception {
//                super("Dictionary");
//                setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//
//                JMenuBar mb = new JMenuBar();
//
//                JMenu mnuDictionary = new JMenu("Dictionary");
//                mb.add(mnuDictionary);
//
//                JMenuItem option = new JMenuItem("Add Word.....");
//                option.setIcon(getImage("add.gif"));
//                option.setAccelerator(KeyStroke.getKeyStroke("F5"));
//                mnuDictionary.add(option);
//                option.addActionListener(new ActionListener() {
//                    public void actionPerformed(ActionEvent e) {
//                        MenuFrame.this.addWord();
//                    }
//                });
//                option = new JMenuItem("Delete Word....");
//                option.setIcon(getImage('delete.gif'));
//                option.setAccelerator(KeyStroke.getKeyStroke("F6"));
//                mnuDictionary.add(option);
//
//                option.addActionListener(new ActionListener() {
//                    public void actionPerformed(ActionEvent e) {
//                        MenuFrame.this.searchWord();
//                    }
//                });
//
//                option = new JMenuItem("List Words");
//                option.setIcon(getImage("List.gif")); // Change Image
//                option.setAccelerator(KeyStroke.getKeyStroke("F8"));
//                mnuDictionary.add(option);
//                option.addActionListener(new ActionListener() {
//                    @Override
//                    public void actionPerformed(ActionEvent e) {
//                        MenuFrame.this.listWords();
//                    }
//                });
//
//                mnuDictionary.addSeparator();
//
//                option = new JMenuItem("Exit");
//                mnuDictionary.add(option);
//                option.addActionListener(new ActionListener() {
//                    @Override
//                    public void actionPerformed(ActionEvent e) {
//                        MenuFrame.this.exit();
//                    }
//                });
//
//                addStorageMenu(mb);
//                addToolBar();
//                setJMenuBar(mb);
//
//                Dictionary.loadFromDisk();
//            }
//
//            public void exit() {
//                if (Dictionary.isModified()) {
//                    int option = JOptionPane.showConfirmDialog(this, "You have some pending" +
//                            "changes. Do you want to write them to disk and then exit?", "Save", 1, 3);
//
//                    if (option == 0) {
//                        Dictionary.saveToDisk();
//                        System.exit(0);
//                    } else if (option == 1) {
//                        System.exit(0);
//                    }
//                } else {
//                    system.exit(0);
//                }
//                public ImageIcon getImage(String filename)
//                {
//
//
//            }
//
//
//
//
//            }
//        }
//    }
//
//    public static void main(String[] args) {
//
//    }
//}
