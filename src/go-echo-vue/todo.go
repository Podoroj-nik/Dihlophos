package main

// Импортирую Фреемворк Echo для работы с Веб
import (
	"github.com/labstack/echo"
)

func main() {
	// Создание нового экземпляра Echo
	e := echo.New()

	// Здесь иы привязываем HTML-файл в котором будет интерфейс Vue JS
	e.File("/", "public/index.html")

	// Запуск веб-сервера
	e.Logger.Fatal(e.Start(":8000"))

}

// Все заработало, можно танцевать!!!
