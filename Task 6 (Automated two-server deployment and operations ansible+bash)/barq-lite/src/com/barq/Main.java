package com.barq;

import java.io.*;
import java.nio.file.*;
import java.time.LocalDateTime;

public class Main {
    private static final String LOG_DIR = "/var/log/barq";
    private static final String LOG_FILE = LOG_DIR + "/barq.log";

    public static void main(String[] args) {
        try {
            // Ensure log directory exists (ok when running as root via systemd)
            Files.createDirectories(Paths.get(LOG_DIR));

            try (FileWriter fw = new FileWriter(LOG_FILE, true)) {
                fw.write("BARQ Lite started at: " + LocalDateTime.now() + "\n");
                fw.flush();
                System.out.println("BARQ Lite app running... logs -> " + LOG_FILE);

                // Simple heartbeat every 5s
                while (true) {
                    fw.write("Heartbeat: " + LocalDateTime.now() + "\n");
                    fw.flush();
                    Thread.sleep(5000);
                }
            }
        } catch (IOException ioe) {
            System.err.println("I/O error writing logs: " + ioe.getMessage());
            ioe.printStackTrace();
        } catch (InterruptedException ie) {
            Thread.currentThread().interrupt();
        }
    }
}
