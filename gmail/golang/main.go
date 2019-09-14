package main

import (
	"log"
	"net/smtp"
	"os"
)

func main() {
	send("hello there")
}

func send(body string) {
	from := os.Getenv("GMAIL_FROM_ADDRESS")
	pass := os.Getenv("GMAIL_PASSWORD")

	if len(os.Args) < 2 {
		log.Fatalf("Invalid argument length: expected=%d, got=%d", 2, len(os.Args))
	}
	to := os.Args[1]

	msg := "From: " + from + "\n" +
		"To: " + to + "\n" +
		"Subject: Hello there\n\n" +
		body

	err := smtp.SendMail("smtp.gmail.com:587",
		smtp.PlainAuth("", from, pass, "smtp.gmail.com"),
		from, []string{to}, []byte(msg))

	if err != nil {
		log.Printf("smtp error: %s", err)
		return
	}

	log.Printf("sent to %s\n", to)
}
