package main

import (
    "fmt"
    "net/http"
    "os"
)

func main() {
    http.HandleFunc("/", homepage)
    port, ok := os.LookupEnv("PORT")
    if !ok {
        port = "8080"
    }
    http.ListenAndServe(":"+port, nil)
}

func homepage(res http.ResponseWriter, req *http.Request) {
    if req.URL.Path != "/" {
        http.NotFound(res, req)
        return
    }
    fmt.Fprintln(res, os.Getenv("TARGET"))
}

