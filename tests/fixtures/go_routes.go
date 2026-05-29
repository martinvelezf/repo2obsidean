package main

import "net/http"

// listUsers is registered via http.HandleFunc below -> should be tagged #route.
func listUsers(w http.ResponseWriter, r *http.Request) {}

// createUser is registered via a gin-style r.POST -> #route.
func createUser(w http.ResponseWriter, r *http.Request) {}

// helper is never registered as a route.
func helper() int { return 1 }

func main() {
	http.HandleFunc("/users", listUsers)
	r := gin.Default()
	r.GET("/health", healthCheck)
	r.POST("/users", createUser)
}

// healthCheck registered via r.GET in another spot.
func healthCheck(w http.ResponseWriter, r *http.Request) {}
