with open('src/auth/Auth.cpp', 'r') as f:
    content = f.read()
content = content.replace('waitForFinished(5000)', 'waitForFinished(300)')
with open('src/auth/Auth.cpp', 'w') as f:
    f.write(content)

with open('src/daemon/Display.h', 'r') as f:
    content = f.read()
content = content.replace(
    'bool m_started { false };',
    'bool m_started { false };\n        bool m_fingerprintAuthActive { false };'
)
with open('src/daemon/Display.h', 'w') as f:
    f.write(content)

with open('src/daemon/Display.cpp', 'r') as f:
    content = f.read()
content = content.replace(
    '        m_auth->setFingerprintlogin(true);\n        startAuth(mainConfig.Fingerprintlogin.User.get(), QString(), session);\n        m_auth->setFingerprintlogin(false);',
    '        m_auth->setFingerprintlogin(true);\n        m_fingerprintAuthActive = true;\n        startAuth(mainConfig.Fingerprintlogin.User.get(), QString(), session);\n        m_auth->setFingerprintlogin(false);'
)
content = content.replace(
    '        if (m_auth->isActive()) {\n            qWarning() << "Existing authentication ongoing, aborting";\n            return false;\n        }',
    '        if (m_auth->isActive()) {\n            if (m_fingerprintAuthActive) {\n                qDebug() << "Stopping fingerprint auth to allow password auth";\n                m_auth->stop();\n                m_fingerprintAuthActive = false;\n            } else {\n                qWarning() << "Existing authentication ongoing, aborting";\n                return false;\n            }\n        }'
)
content = content.replace(
    '    void Display::slotAuthenticationFinished(const QString &user, bool success) {\n        if (m_auth->autologin() && !success) {',
    '    void Display::slotAuthenticationFinished(const QString &user, bool success) {\n        m_fingerprintAuthActive = false;\n        if (m_auth->autologin() && !success) {'
)
with open('src/daemon/Display.cpp', 'w') as f:
    f.write(content)

print("Parallel auth fix applied.")
