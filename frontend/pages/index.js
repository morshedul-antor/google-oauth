import styles from "../styles/Home.module.css";
import google from "../assets/search.png";
import Image from "next/image";

import React from "react";

export default function Home() {
  const handleLogin = () => {
    window.location.href = "http://localhost:8000/auth/login";
  };

  return (
    <div className={styles.container}>
      <div className={styles.main}>
        <button
          onClick={handleLogin}
          style={{ display: "flex", alignItems: "center" }}
        >
          <Image
            src={google}
            alt="Google Logo"
            style={{ width: "20px", height: "20px", marginRight: "10px" }}
          />
          Sign in with Google
        </button>
      </div>
    </div>
  );
}
