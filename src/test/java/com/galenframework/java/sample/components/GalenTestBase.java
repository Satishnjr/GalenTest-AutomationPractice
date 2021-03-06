package com.galenframework.java.sample.components;

import static java.util.Arrays.asList;

import java.util.List;

import org.openqa.selenium.Dimension;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebDriverException;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.DataProvider;

import com.galenframework.testng.GalenTestNgTestBase;

public abstract class GalenTestBase extends GalenTestNgTestBase {

	private static final String ENV_URL = "http://automationpractice.com/index.php";

	static WebDriver driver;

	@Override
	public WebDriver createDriver(Object[] args) {
		System.setProperty("webdriver.chrome.driver", "C:\\chrome-driver\\chromedriver.exe");
		driver = new ChromeDriver();
		
		if (args.length > 0) {
			if (args[0] != null && args[0] instanceof TestDevice) {
				TestDevice device = (TestDevice) args[0];
				if (device.getScreenSize() != null) {
					driver.manage().window().setSize(device.getScreenSize());
					
				}
			}
		}
		return driver;
	}

	public void load(String uri) {
		getDriver().get(ENV_URL + uri);
	}

	@DataProvider(name = "devices")
	public Object[][] devices() {
		return new Object[][] { { new TestDevice("mobile", new Dimension(450, 800), asList("mobile")) },
				{ new TestDevice("tablet", new Dimension(750, 800), asList("tablet")) },
				{ new TestDevice("desktop", new Dimension(1300, 800), asList("desktop")) } };
	}

	public static class TestDevice {
		private final String name;
		private final Dimension screenSize;
		private final List<String> tags;

		public TestDevice(String name, Dimension screenSize, List<String> tags) {
			this.name = name;
			this.screenSize = screenSize;
			this.tags = tags;
		}

		public String getName() {
			return name;
		}

		public Dimension getScreenSize() {
			return screenSize;
		}

		public List<String> getTags() {
			return tags;
		}

		@Override
		public String toString() {
			return String.format("%s %dx%d", name, screenSize.width, screenSize.height);
		}

		
		

	}
}
