// Client-side JavaScript to send an offer
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    // Create a peer connection and add stream
    const pc = new RTCPeerConnection();
    stream.getTracks().forEach(track => pc.addTrack(track, stream));

    // Create an offer
    pc.createOffer().then(offer => {
      return pc.setLocalDescription(new RTCSessionDescription({ type: 'offer', sdp: offer }));
    }).then(() => {
      // Send the offer to the server
      fetch('/offer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          sdp: pc.localDescription.sdp,
          type: pc.localDescription.type
        })
      }).then(response => response.json())
      .then(data => {
        // Handle the answer from the server
        pc.setRemoteDescription(new RTCSessionDescription({ type: data.type, sdp: data.sdp }));
      });
    });
  })
  .catch(error => console.error("Error accessing camera:", error));
