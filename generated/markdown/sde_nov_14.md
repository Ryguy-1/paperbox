# Introduction to JavaFX 17

JavaFX is a software platform for creating and running desktop GUI applications. It was introduced by Oracle in 2012 as part of the Java Platform, Standard Edition (Java SE). The latest version, JavaFX 17, offers several enhancements and improvements over previous versions, making it an attractive choice for developers looking to create modern, responsive, and visually appealing desktop applications.

Some key features of JavaFX 17 include:

1. Enhanced performance: JavaFX 17 provides better performance through optimizations and improved rendering capabilities, enabling developers to create smooth and fast user interfaces.

2. Improved modularity: The platform now follows the Java Module System (JMS), allowing for easier integration with other Java libraries and frameworks. This promotes a more modular approach to application development.

3. CSS Styling: JavaFX 17 supports CSS styling, making it simpler to apply consistent styles across an entire application or individual components.

4. Responsive design: The platform offers built-in support for responsive design, allowing developers to create applications that adapt seamlessly to different screen sizes and devices.

5. Rich set of controls: JavaFX 17 provides a comprehensive library of user interface controls, including buttons, labels, text fields, and more, enabling developers to quickly build professional-looking applications.

Overall, JavaFX 17 is an excellent choice for developers looking to create modern, responsive, and visually appealing desktop GUI applications with minimal effort.

## JavaFX 17 Elements Relationships

JavaFX is a software platform for creating desktop applications with a rich visual experience. It provides developers with a set of elements to build user interfaces, including stage, scene, and pane. In this section, we will cover these three key elements with super short code examples and their relationships.

1. Stage: The stage represents the main window or dialog box of an application. It is responsible for managing the life cycle of the application and providing a container for scenes.

Example:
```java
import javafx.application.Application;
import javafx.stage.Stage;

public class MyApp extends Application {
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        // Create a scene and show the stage
        Scene scene = new Scene(new Pane());
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}
```

2. Scene: A scene is a visual container that holds all the graphical elements, such as nodes, shapes, and controls, which make up the user interface of an application. It is responsible for managing the layout and rendering of these elements.

Example:
```java
import javafx.scene.Scene;
import javafx.scene.layout.Pane;

public class MyScene extends Scene {
    public MyScene(Pane root) {
        super(root);
    }
}
```

3. Pane: A pane is a container node that holds other nodes, such as shapes and controls, to organize the layout of an application's user interface. It can be used to create custom layouts or group related elements together.

Example:
```java
import javafx.scene.layout.Pane;

public class MyPane extends Pane {
    public MyPane() {
        // Add nodes to the pane
        Scene scene = new Scene(this);
        Stage stage = new Stage();
        stage.setScene(scene);
        stage.show();
    }
}
```

In summary, JavaFX provides developers with essential elements like stage, scene, and pane for creating rich user interfaces in desktop applications. By understanding these key components and their relationships, developers can create visually appealing and functional applications.

HBox is a layout container in JavaFX that arranges its children horizontally. It is useful for organizing horizontal layouts and aligning elements within the scene. To use HBox, you can add it as a child of the Scene object or any other layout node:

Example:
```java
import javafx.scene.Scene;
import javafx.scene.layout.HBox;

public class MyHBox extends HBox {
    public MyHBox(Node... nodes) {
        super(nodes);
    }
}
```

In this example, the MyHBox constructor takes an array of Node objects and adds them as children to the HBox. This allows developers to create a horizontal layout with multiple elements within their application's user interface.

## Start Method

The `start` method is a crucial component of the JavaFX framework, specifically in version 17. It is responsible for initializing and launching the application's main window or stage. This method is called automatically when an application is started, allowing developers to set up their user interface and perform necessary tasks before presenting it to the end-user.

To use the `start` method in JavaFX 17, follow these simple steps:

1. Create a subclass of the Application class, which serves as the main entry point for your application.
2. Override the `start` method in this subclass.
3. Implement the desired functionality within the `start` method, such as setting up the stage, adding nodes to the scene graph, and handling events.
4. Call the super class's `start` method within your overridden implementation to ensure proper initialization of the Application framework.

For example:

```java
public class MyApplication extends Application {
    @Override
    public void start(Stage primaryStage) {
        // Set up the stage and scene graph
        Scene scene = new Scene(new Group(), 300, 250);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

In this example, the `start` method is called automatically when the application starts, setting up the stage and scene graph before presenting it to the user.

Please refer to the Google Drive folder for McBurney's example to further understand how to implement the `start` method in JavaFX 17.

## Build.gradle for JavaFX 17

- Refer to McBurney notes for build.gradle configuration with JavaFX 17 support

## Command Line Arguments for --add-modules for JavaFX

The `--add-modules` option in the JavaFX command line is used to specify which modules should be included in the application. This can be useful when you want to control which modules are loaded during runtime, ensuring that only necessary modules are utilized. To use this option, follow these steps:

1. Specify the module names or patterns using the `--add-modules` argument. For example:

```bash
java --module-path <path_to_modules> --add-modules javafx.controls,javafx.fxml
```

2. Use wildcards to include multiple modules. For instance:

```bash
java --module-path <path_to_modules> --add-modules javafx.base,javafx.controls,javafx.graphics
```

3. Combine the `--add-modules` option with other command line options to create a more complex configuration. For example:

```bash
java --module-path <path_to_modules> --add-modules javafx.base,javafx.controls,javafx.graphics --module-path <path_to_other_modules> --add-modules other.module1,other.module2
```

Remember to adjust the paths and module names according to your project's structure and requirements.

## Section with start method that has stage.setTitle("Hello World");

To create a section with a start method that has `stage.setTitle("Hello World")`, follow these steps in one code block:

```java
public class HelloWorld extends Application {
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage stage) throws Exception {
        stage.setTitle("Hello World");
        private Label text = new Label();
        private FlowPane root = new FlowPane();

        root.getChildren().add(text);

        Scene scene = new Scene(root, 200, 200);

        stage.setScene(scene);

        stage.show();
    }
}
```
Note: The FlowPane is a layout pane that arranges its children in a flow-like manner, either horizontally or vertically depending on the preferred direction property.

## JavaFX Button

A JavaFX button is a graphical control element that allows users to interact with an application by clicking on it. To create and use a JavaFX button, you can follow these simple steps:

1. Create a stage and scene:
```java
Stage primaryStage = new Stage();
Scene scene = new Scene(new Group(), 300, 250);
primaryStage.setScene(scene);
primaryStage.show();
```

2. Add a button to the scene:
```java
Button button = new Button("Click Me");
scene.getRoot().addChild(button);
```

3. Create a button handler:
```java
public void handleButtonAction(ActionEvent event) {
    System.out.println("Button clicked!");
}
```

4. Add the button handler to the button:
```java
button.setOnAction(event -> handleButtonAction(event));
```

5. Place the code in the `start()` method:
```java
public void start(Stage primaryStage) {
    ...
}
```

Note: You can just put code directly within lambda body if desired.

## Example of Exception Handling with Button in JavaFX 17

To demonstrate exception handling with a button in JavaFX 17, let's create a simple example. We will set the button text to one value if the calculation is successful and another if it fails. The calculation we will perform is finding the square root of a number and clicking the button.

```java
package com.example;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class ExceptionHandlingExample extends Application {
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        StackPane root = new StackPane();
        root.setAlignment(Pos.CENTER);

        Button button = new Button("Click to Calculate Sqrt");
        button.setOnAction(event -> {
            try {
                double number = Double.parseDouble(button.getText().replaceAll("[^0-9]", ""));
                button.setText("Calculated: " + Math.sqrt(number));
            } catch (NumberFormatException e) {
                button.setText("Invalid Input");
            }
        });

        Scene scene = new Scene(root, 300, 250);
        primaryStage.setTitle("Exception Handling Example");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}
```

In this example, we create a JavaFX application that has a button with the text "Click to Calculate Sqrt". When the user clicks on the button, it will attempt to parse the number from the button's text and calculate the square root. If the input is not a valid number, an exception will be thrown, and the button text will be updated accordingly.

## JavaFX ActionHandler Method with e.getSource()

In this section, we will discuss a JavaFX action handler method that uses the `e.getSource()` function to change the color of a button that called it. We will implement this in one class.

First, let's create a custom `ActionHandler` class:

```java
public class ColorChangeActionHandler implements ActionEvent {
    public void handle(ActionEvent e) {
        Button sourceButton = (Button) e.getSource();
        sourceButton.setStyle("-fx-background-color: red;");
    }
}
```

Now, we will create a `Main` class to set up the JavaFX application and add the action handler to a button:

```java
public class Main extends Application {
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        Button button = new Button("Change Color");
        button.setOnAction(new ColorChangeActionHandler());

        Scene scene = new Scene(button, 300, 250);
        primaryStage.setTitle("Color Change Example");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}
```

When the "Change Color" button is clicked, the `handle()` method in the `ColorChangeActionHandler` class will be called, and it will change the color of the button to red using the `e.getSource()` function.

## Project Aesthetics

- The aesthetics bar isn't super high, so we should strive for a balance between functionality and visual appeal.
- Avoid using default formatting too much; instead, opt for a consistent style that reflects the project's goals and target audience.
- Consider using colors, fonts, and icons to enhance readability and create a cohesive look across all elements of the project.
- Tao is cool.

