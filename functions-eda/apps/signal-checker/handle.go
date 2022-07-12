package function

import (
	"context"
	"encoding/json"
	"fmt"

	cloudevents "github.com/cloudevents/sdk-go/v2"
)

type DroneDataReceived struct {
	DroneId string
	Signal  float32
}

// Handle an event.
func Handle(ctx context.Context, event cloudevents.Event) (*cloudevents.Event, error) {
	fmt.Printf("Incoming Event: \n%v\n", event)

	eventData, err := parseEventData(event)

	if err != nil {
		fmt.Printf("%v\n", err)
		return nil, err
	}

	outputEvent := cloudevents.NewEvent()
	outputEvent.SetSource("signal-checker")
	outputEvent.SetType("DroneSignalVerified")

	if eventData.Signal < 10 {
		fmt.Printf("Low signal detected [DroneId %v, Signal: %v%%]\n", eventData.DroneId, eventData.Signal)
	}

	return &outputEvent, nil
}

func parseEventData(event cloudevents.Event) (DroneDataReceived, error) {
	eventData := DroneDataReceived{}
	if err := json.Unmarshal([]byte(event.Data()), &eventData); err != nil {
		return DroneDataReceived{}, err
	}

	return eventData, nil
}
