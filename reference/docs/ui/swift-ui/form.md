---
title: "Form"
description: "A SwiftUI Form component for collecting user input in a structured layout."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/form.md"
scraped_at: "2026-07-15T08:59:16.790525"
---

---
title: Form
description: A SwiftUI Form component for collecting user input in a structured layout.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Form

A SwiftUI Form component for collecting user input in a structured layout.
iOS, tvOS, Included in Expo Go

Expo UI Form matches the official SwiftUI [Form API](https://developer.apple.com/documentation/swiftui/form). It provides a container for grouping controls used for data entry, such as in settings or inspection panes.

## Installation

```sh
# npm
npx expo install @expo/ui

# yarn
yarn expo install @expo/ui

# pnpm
pnpm expo install @expo/ui

# bun
bun expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

### Basic form

```tsx
import { useState } from 'react';
import { Host, Form, TextField } from '@expo/ui/swift-ui';

export default function BasicFormExample() {
  return (
    <Host style={{ flex: 1 }}>
      <Form>
        <TextField placeholder="Enter your name" />
      </Form>
    </Host>
  );
}
```

### Form with sections

Use the [`Section`](/versions/latest/sdk/ui/swift-ui/section.md) component to group related controls within a form.

```tsx
import { useState } from 'react';
import { Host, Form, Section, TextField, Toggle, Button } from '@expo/ui/swift-ui';

export default function FormWithSectionsExample() {
  const [notifications, setNotifications] = useState(false);
  const [darkMode, setDarkMode] = useState(false);

  return (
    <Host style={{ flex: 1 }}>
      <Form>
        <Section title="Profile">
          <TextField placeholder="Name" />
          <TextField placeholder="Email" />
        </Section>

        <Section title="Preferences">
          <Toggle
            label="Enable notifications"
            isOn={notifications}
            onIsOnChange={setNotifications}
          />
          <Toggle label="Dark mode" isOn={darkMode} onIsOnChange={setDarkMode} />
        </Section>

        <Section>
          <Button label="Save Changes" onPress={() => console.log('Saved!')} />
        </Section>
      </Form>
    </Host>
  );
}
```

### Form with custom background

Use the `scrollContentBackground` modifier to customize or hide the form's background.

```tsx
import { useState } from 'react';
import { Host, Form, Section, TextField } from '@expo/ui/swift-ui';
import { scrollContentBackground, background } from '@expo/ui/swift-ui/modifiers';

export default function FormBackgroundExample() {
  return (
    <Host style={{ flex: 1 }}>
      <Form modifiers={[scrollContentBackground('hidden'), background('#F0F0F0')]}>
        <Section title="Custom Background">
          <TextField placeholder="Enter text" />
        </Section>
      </Form>
    </Host>
  );
}
```

### Non-scrollable form

Use the [`scrollDisabled`](/versions/latest/sdk/ui/swift-ui/modifiers.md#scrolldisableddisabled) modifier to prevent the form from scrolling.

> **Note:** The `scrollDisabled` modifier is only available on iOS 16+ and tvOS 16+.

```tsx
import { useState } from 'react';
import { Host, Form, Section, TextField, Toggle } from '@expo/ui/swift-ui';
import { scrollDisabled } from '@expo/ui/swift-ui/modifiers';

export default function NonScrollableFormExample() {
  const [isOn, setIsOn] = useState(false);

  return (
    <Host style={{ flex: 1 }}>
      <Form modifiers={[scrollDisabled()]}>
        <Section title="Settings">
          <Toggle label="Enable feature" isOn={isOn} onIsOnChange={setIsOn} />
        </Section>
      </Form>
    </Host>
  );
}
```

### Pull-to-refresh form

Use the `refreshable` modifier to add pull-to-refresh functionality.

```tsx
import { useState, useCallback } from 'react';
import { Host, Form, Section, Text } from '@expo/ui/swift-ui';
import { refreshable } from '@expo/ui/swift-ui/modifiers';

export default function RefreshableFormExample() {
  const [lastRefresh, setLastRefresh] = useState(new Date());

  const handleRefresh = useCallback(async () => {
    // Simulate network request
    await new Promise(resolve => setTimeout(resolve, 1500));
    setLastRefresh(new Date());
  }, []);

  return (
    <Host style={{ flex: 1 }}>
      <Form modifiers={[refreshable(handleRefresh)]}>
        <Section title="Pull to Refresh">
          <Text>Last refreshed: {lastRefresh.toLocaleTimeString()}</Text>
        </Section>
      </Form>
    </Host>
  );
}
```

## API

```tsx
import { Form } from '@expo/ui/swift-ui';
```

## Component

### `Form`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[FormProps](#formprops)\>

FormProps

### `children`

Supported platforms: iOS, tvOS.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

The content of the form.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
