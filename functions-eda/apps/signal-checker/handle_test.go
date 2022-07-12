package function

import (
	"context"
	"encoding/json"
	"testing"

	"github.com/cloudevents/sdk-go/v2/event"
	cloudevents "github.com/cloudevents/sdk-go/v2/event"
)

// TestHandle ensures that Handle accepts a valid CloudEvent without error.
func TestHandle(t *testing.T) {
	// A minimal, but valid, event.
	event := event.New()
	event.SetID("TEST-EVENT-01")
	event.SetType("DroneDataReceived")
	event.SetSource("http://localhost:8080/")
	input := `{ "droneId": 1234, "signal": 4.3 }`
	event.SetData(cloudevents.ApplicationJSON, &input)
	// Invoke the defined handler.
	ce, err := Handle(context.Background(), event)
	if err != nil {
		t.Fatal(err)
	}

	if ce == nil {
		t.Errorf("The output CloudEvent cannot be nil")
	}
	if ce.Type() != "DroneSignalVerified" {
		t.Errorf("Wrong CloudEvent Type received: %v , expected DroneSignalVerified", ce.Type())
	}

	output := ""
	err = json.Unmarshal(ce.Data(), &output)
	if err != nil {
		t.Fatal(err)
	}

}
